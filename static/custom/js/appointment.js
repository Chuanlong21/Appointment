// Function to populate start time options

function populateStartTimeOptions(selectId, startHour, endHour, intervalMinutes) {
    var startTimeSelect = document.getElementById(selectId);
    for (var hour = startHour; hour <= endHour; hour++) {
        for (var minute = 0; minute < 60; minute += intervalMinutes) {
            var time = `${hour.toString().padStart(2, '0')}:${minute.toString().padStart(2, '0')}`;
            var option = document.createElement('option');
            option.value = time;
            option.text = time;
            startTimeSelect.add(option);
        }
    }
}

function submitForm(event) {
    event.preventDefault(); // Prevent the default form submission

    // Gather form data
    const form = document.getElementById('appointment-form');
    const formData = new FormData(form);


    const jsonData = {};
    formData.forEach((value, key) => {
        jsonData[key] = value;
    });


    // Send the form data as JSON
    fetch('/addEvent', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
        .then(response => response.json())
        .then(data => {
            handleResponse(data)
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function handleResponse(data) {

    const startTime = data.startTime; // assuming format "HH:MM"
    const endTime = data.endTime; // assuming format "HH:MM"
     const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0'); // 月份从0开始，所以需要+1
    const day = String(today.getDate()).padStart(2, '0');
    const formattedDate = `${year}-${month}-${day}`;

    // Convert to FullCalendar event format
    const event = {
        start: `${formattedDate}T${startTime}:00`, // adjust date format as needed
        end: `${formattedDate}T${endTime}:00` // adjust date format as needed
    };

    addEventToCalendar(event);
}


//EventListener
document.addEventListener('DOMContentLoaded', function () {
    const submitButton = document.getElementById('submit-button');
    submitButton.addEventListener('click', function (event) {
        submitForm(event);
    });
});

//Functions Call
populateStartTimeOptions('validationDefault05', 8, 22, 60);