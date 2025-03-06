document.addEventListener("DOMContentLoaded", function () {
    // Line Chart
    const lineCtx = document.getElementById("lineChart").getContext("2d");
    const lineData = [10, 20, 15, 30, 40, 25, 50];
    const lineChart = new Chart(lineCtx, {
        type: "line",
        data: {
            labels: ["AI & ML", "Blockchain", "Mobile", "FinTech", "Others"],
            datasets: [
                {
                    label: "Dynamic Enrollments",
                    data: lineData,
                    backgroundColor: "rgba(255, 87, 34, 0.2)",
                    borderColor: "#ff5722",
                    borderWidth: 2,
                    tension: 0.4,
                },
            ],
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false },
            },
            scales: { y: { beginAtZero: true } },
        },
    });

    // Bar Chart (20 bins)
    const barCtx = document.getElementById("barChart").getContext("2d");
    const bins = Array.from({ length: 20 }, (_, i) => i + 1);
    const binData = Array.from({ length: 20 }, () => Math.floor(Math.random() * 100));
    const barChart = new Chart(barCtx, {
        type: "bar",
        data: {
            labels: bins,
            datasets: [
                {
                    label: "Category Distribution",
                    data: binData,
                    backgroundColor: "rgba(54, 162, 235, 0.8)",
                    borderColor: "#36a2eb",
                    borderWidth: 1,
                },
            ],
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false },
            },
            scales: { y: { beginAtZero: true } },
        },
    });

    // Simulate Real-Time Updates
    setInterval(() => {
        lineData.forEach((_, i) => (lineData[i] += Math.floor(Math.random() * 15)));
        lineChart.update();

        binData.forEach((_, i) => (binData[i] = Math.floor(Math.random() * 100)));
        barChart.update();
    }, 2000);
});
