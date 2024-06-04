document.addEventListener('DOMContentLoaded', function () {

    var events =
        {
            title: 'Cogent Social',
            start: '2024-05-31T12:00:00',
            end: '2024-05-31T13:00:00',
            url: 'https://url1'
        };
        // add more events here

    addEventToCalendar(events);

});


let globalEvents = []; // 全局变量存储事件

function addEventToCalendar(event) {
    globalEvents.push(event); // 添加事件到全局变量
    renderCalendar(); // 渲染日历
}

function renderCalendar() {
    const calendarEl = document.getElementById('calendar');
    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'timeGridWeek',
        initialDate: new Date(), // Set the initial date to today
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'timeGridDay,timeGridWeek'
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
        events: globalEvents, // 使用全局变量存储的事件
        eventClick: function (info) {
            info.jsEvent.preventDefault(); // 阻止默认事件
            if (info.event.url) {
                window.open(info.event.url); // 打开事件 URL
            }
        },
    });

    calendar.render();
}