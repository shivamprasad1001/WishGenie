const targetDate = new Date("2025-01-20T00:00:00").getTime();
const countdownElement = document.getElementById('countdown');

setInterval(() => {
    const now = new Date().getTime();
    const diff = targetDate - now;

    if (diff <= 0) {
        countdownElement.innerText = "The time has arrived!";
        return;
    }

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);

    countdownElement.innerText = `Time left: ${days}d ${hours}h ${minutes}m ${seconds}s`;
}, 1000);
