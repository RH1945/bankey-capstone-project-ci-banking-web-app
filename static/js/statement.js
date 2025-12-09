document.addEventListener("DOMContentLoaded", function () {

    const tableBody = document.getElementById("statement-body");
    const loadMoreBtn = document.getElementById("load-more");

    if (!loadMoreBtn) return;

    const cardNumber = loadMoreBtn.dataset.card;
    let page = 1;

    const modal = document.getElementById("tx-modal");
    const closeBtn = document.getElementById("tx-close");

    const mRef = document.getElementById("m-ref");
    const mSender = document.getElementById("m-sender");
    const mReceiver = document.getElementById("m-receiver");
    const mAmount = document.getElementById("m-amount");
    const mDate = document.getElementById("m-date");

    // -------- LOAD MORE TRANSACTIONS --------
    function loadTransactions() {
        fetch(`/account/statement/${cardNumber}/?page=${page}`, {
            headers: {"X-Requested-With": "XMLHttpRequest"}
        })
            .then(response => response.json())
            .then(data => {

                data.transactions.forEach(tx => {
                    const row = document.createElement("tr");
                    row.classList.add("tx-row");

                    row.dataset.sender = tx.sender;
                    row.dataset.receiver = tx.receiver;
                    row.dataset.amount = tx.amount;
                    row.dataset.reference = tx.reference;
                    row.dataset.date = tx.timestamp;

                    row.innerHTML = `
                    <td>${tx.reference}</td>
                    <td>${tx.sender}</td>
                    <td>${tx.receiver}</td>
                    <td>£${tx.amount}</td>
                    <td>${tx.timestamp}</td>
                `;

                    tableBody.appendChild(row);
                });

                if (!data.has_next) {
                    loadMoreBtn.style.display = "none";
                }

                page++;
            });
    }

    loadMoreBtn.addEventListener("click", loadTransactions);

    // -------- OPEN MODAL (EVENT DELEGATION) --------
    tableBody.addEventListener("click", function (e) {
        const row = e.target.closest(".tx-row");
        if (!row) return;

        mRef.textContent = row.dataset.reference;
        mSender.textContent = row.dataset.sender;
        mReceiver.textContent = row.dataset.receiver;
        mAmount.textContent = row.dataset.amount;
        mDate.textContent = row.dataset.date;

        modal.classList.remove("hidden");
    });

    // -------- CLOSE MODAL --------
    closeBtn.addEventListener("click", function () {
        modal.classList.add("hidden");
    });

    modal.addEventListener("click", function (e) {
        if (e.target === modal) {
            modal.classList.add("hidden");
        }
    });

});
