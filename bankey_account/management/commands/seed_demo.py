import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from bankey_account.models import BankeyAccount, Card, Transaction
from bankey_account.utils import generate_expiration_date
from django.utils import timezone

User = get_user_model()


class Command(BaseCommand):
    help = "Seed database with users, accounts, cards, and transactions."

    def add_arguments(self, parser):
        parser.add_argument("--users", type=int, default=5)
        parser.add_argument("--transactions", type=int, default=25)
        parser.add_argument("--with-superuser", action="store_true")
        parser.add_argument("--wipe-only", action="store_true")

    def handle(self, *args, **options):

        user_count = options["users"]
        tx_count = options["transactions"]

        # ----------------------------------------------------
        # OPTIONAL: WIPE ONLY (NO NEW DATA)
        # ----------------------------------------------------
        if options["wipe_only"]:
            self.stdout.write(self.style.WARNING("Wiping database…"))
            Transaction.objects.all().delete()
            Card.objects.all().delete()
            BankeyAccount.objects.all().delete()
            User.objects.exclude(is_superuser=True).delete()
            self.stdout.write(self.style.SUCCESS("Done — data wiped clean."))
            return

        # ----------------------------------------------------
        # FULL DELETE BEFORE SEEDING
        # ----------------------------------------------------
        self.stdout.write(self.style.WARNING("Wiping existing data…"))
        Transaction.objects.all().delete()
        Card.objects.all().delete()
        BankeyAccount.objects.all().delete()
        User.objects.exclude(is_superuser=True).delete()

        # ----------------------------------------------------
        # CREATE SUPERUSER IF REQUESTED
        # ----------------------------------------------------
        if options["with_superuser"]:
            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    username="admin",
                    password="admin123",
                    email="admin@example.com",
                    first_name="Admin",
                    last_name="User"
                )
                self.stdout.write(self.style.SUCCESS("Superuser: admin / admin123"))
            else:
                self.stdout.write("Superuser already exists.")

        # ----------------------------------------------------
        # RANDOM USERS
        # ----------------------------------------------------
        first_names = ["Juan", "Maria", "Luis", "Ana", "Carla", "Mario", "Jose", "Lucia", "Rafael", "Diana"]
        last_names = ["Gomez", "Lopez", "Martinez", "Garcia", "Ruiz", "Hernandez", "Torres", "Diaz", "Fernandez", "Suarez"]

        self.stdout.write(f"Creating {user_count} users…")
        created_users = []

        for i in range(user_count):

            fn = random.choice(first_names)
            ln = random.choice(last_names)

            username = f"{fn.lower()}{ln.lower()}{i}"
            email = f"{username}@example.com"
            raw_password = "pass1234"

            # Safe random DOB
            dob = date.today() - timedelta(days=random.randint(20*365, 60*365))

            user = User.objects.create_user(
                username=username,
                password=raw_password,
                email=email,
                first_name=fn,
                last_name=ln,
            )

            # store DOB if supported
            if hasattr(user, "date_of_birth"):
                user.date_of_birth = dob
                user.save()

            created_users.append(user)

            # Print each user's login credentials
            self.stdout.write(
                self.style.SUCCESS(f"User created: {email} / {raw_password}")
            )

        # ----------------------------------------------------
        # CREATE ACCOUNTS + CARDS
        # ----------------------------------------------------
        self.stdout.write("Creating accounts + cards…")

        for user in created_users:

            account = BankeyAccount.objects.create(
                user=user,
                acc_type=random.choice([0, 1]),  # Personal / Business
                currency="GBP",
            )

            # Each user gets 1–2 cards
            num_cards = random.randint(1, 2)

            for _ in range(num_cards):
                card = Card.objects.create(
                    account=account,
                    card_type=random.choice([0, 1]),  # Debit / Credit
                    expiration_date=generate_expiration_date(),
                    card_balance=200,  # Start with demo balance
                )

            # 🔥 IMPORTANT: UPDATE ACCOUNT BALANCE AFTER CARDS
            account.update_balance()
            account.save()

        self.stdout.write(self.style.SUCCESS("Accounts and cards created."))

        # ----------------------------------------------------
        # RANDOM TRANSACTIONS
        # ----------------------------------------------------
        self.stdout.write(f"Generating {tx_count} transactions…")

        all_users = list(User.objects.exclude(is_superuser=True))

        for _ in range(tx_count):

            sender_user = random.choice(all_users)
            receiver_user = random.choice(all_users)

            # Avoid self-sending
            while receiver_user == sender_user:
                receiver_user = random.choice(all_users)

            sender_account = sender_user.bankeyaccount_set.first()
            if not sender_account:
                continue

            sender_cards = sender_account.card_set.all()
            if not sender_cards:
                continue

            sender_card = random.choice(list(sender_cards))

            amount = random.randint(1, 50)

            # Skip if insufficient balance
            if sender_card.card_balance < amount:
                continue

            # Update sender
            sender_card.card_balance -= amount
            sender_card.save()

            # Update receiver
            receiver_card = Card.objects.filter(account__user=receiver_user).first()
            if receiver_card:
                receiver_card.card_balance += amount
                receiver_card.save()
                receiver_card.account.update_balance()
                receiver_card.account.save()

            # Save transaction
            Transaction.objects.create(
                sender=sender_user,
                receiver=receiver_user,
                amount=amount,
                reference=f"Seed Payment #{random.randint(1000,9999)}",
                timestamp=timezone.now(),
                card=sender_card,
            )

            # Sync sender account balance
            sender_account.update_balance()
            sender_account.save()

        self.stdout.write(self.style.SUCCESS("Transactions created successfully."))
        self.stdout.write(self.style.SUCCESS("🌱 Database seeding complete!"))
