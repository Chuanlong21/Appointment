
async function fetchEvents() {
    try {
        const response = await fetch('/employee');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return await response.json();
    } catch (error) {
        console.error('Error fetching events:', error);
        return [];
    }
}

document.addEventListener('DOMContentLoaded', function () {
    renderCalendar();
});




async function renderCalendar() {
    const events = await fetchEvents()

    const calendarEl = document.getElementById('calendar');
    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'timeGridDay',
        initialDate: new Date(), // Set the initial date to today
        headerToolbar: {
            left: '',
            center: 'title',
            right: ''
        },
        businessHours: {
            daysOfWeek: [1, 2, 3, 4, 5, 6], // 周一到周六
            startTime: '08:00', // 营业开始时间
            endTime: '22:00' // 营业结束时间
        },
        allDaySlot: false,
        height: 'auto', // Adjust height to fit the container
        aspectRatio: 1.5, // Adjust the aspect ratio to fit the container
        slotMinTime: '08:00:00', // 日历最早显示时间
        slotMaxTime: '22:00:00', // 日历最晚显示时间
        events: events,
        eventClick: function (info) {
            info.jsEvent.preventDefault(); // 阻止默认事件
            if (info.event.url) {
                window.open(info.event.url); // 打开事件 URL
            }
        },
    });

    calendar.render();
}