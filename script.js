const ws = new WebSocket("ws://127.0.0.1:8000/ws");

const statusBox = document.getElementById("status-box");
const statusText = document.getElementById("status-text");

let lastStatus = "";
let lastUpdateTime = 0;
const HOLD_TIME = 2000; // 2 seconds

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    const newStatus = data.status;

    const now = Date.now();

    //Prevent flickering (hold for 2 seconds)
    if (newStatus !== lastStatus && now - lastUpdateTime < HOLD_TIME) {
        return;
    }

    lastStatus = newStatus;
    lastUpdateTime = now;

    // Reset classes
    statusBox.className = "";

    if (newStatus === "NORMAL") {
        statusBox.classList.add("normal");
        statusText.innerText = "Student is Focused";
    }
    else if (newStatus === "HAPPY") {
        statusBox.classList.add("happy");
        statusText.innerText = "Student is Happy / Engaged";
    }
    else if (newStatus === "CONFUSED") {
        statusBox.classList.add("confused");
        statusText.innerText = "Student is Confused";
    }
    else if (newStatus === "SUSPICIOUS") {
        statusBox.classList.add("suspicious");
        statusText.innerText = "⚠Alert";
    }
};

ws.onerror = () => {
    statusText.innerText = "Connection Error";
};
