async function loadDashboard() {

    const response = await fetch("http://127.0.0.1:8000/dashboard");
    // http://127.0.0.1:8000/dashboard

    const data = await response.json();
    console.log(data);

    document.getElementById("members").innerHTML = data.total_members;
    document.getElementById("trainers").innerHTML = data.total_trainers;

    document.getElementById("plans").innerHTML = data.total_plans;

    document.getElementById("attendence").innerHTML = data.total_attendence;

}

window.onload = loadDashboard;