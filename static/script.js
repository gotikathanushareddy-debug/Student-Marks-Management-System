
document.getElementById("marksForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const student = {
        name: document.getElementById("name").value,
        marks: [
            Number(document.getElementById("m1").value),
            Number(document.getElementById("m2").value),
            Number(document.getElementById("m3").value)
        ]
    };

    try {
        const response = await fetch("/calculate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(student)
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong");
        }

        document.getElementById("result").innerHTML =
            "Student: " + data.name +
            "<br>Total: " + data.total +
            "<br>Average: " + data.average +
            "<br>Grade: " + data.grade +
            "<br>Status: " + data.status;

    } catch (error) {
        document.getElementById("result").textContent = error.message;
    }
});
