document.addEventListener("DOMContentLoaded", function () {
    const tableBody = document.getElementById("statement-body");
    const loadMoreBtn = document.getElementById("load-more");
    const cardNumber = loadMoreBtn.dataset.card;
    let page = 1;

    function loadTransactions() {
        fetch(`/statement/${cardNumber}/?page=${page}`, {
            headers: { "X-Requested-With": "XMLHttpRequest" }
        })
        .then(response => response.json())
        .then(data => {
            data.transactions.forEach(tx => {
                const row = document.createElement("tr");

                row.innerHTML = `
                    <td>${tx.timestamp}</td>
                    <td>${tx.sender}</td>
                    <td>${tx.receiver}</td>
                    <td>${tx.reference}</td>
                    <td>£${tx.amount}</td>
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
});
