// https://grok.com/chat/1d7a419d-897f-42ed-9e58-5cad7f27ac79
// Chart.js Configurations
        const colors = [
            '#2FDD92', '#548CFF', '#D1FFA2', '#4FD3C4', '#28ABB9', '#7FDBDA',
            '#B2D3BE', '#3D93A3', '#09A8FA', '#7DACE4'
        ];

        // Chart 1: Family Type Distribution (bar)
        new Chart(document.getElementById('familyTypeChart'), {
            type: 'bar',
            data: {
                labels: ['یتیم', 'زندانی', 'مطلقه', 'رها شده', 'بیمار', 'فقیر'],
                datasets: [{
                    label: 'تعداد خانواده‌ها',
                    data: [30, 20, 15, 10, 12, 25],
                    backgroundColor: colors,
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { position: 'top' }, title: { display: false, text: 'توزیع خانواده‌ها بر اساس نوع نیازمندی' } },
                scales: { y: { beginAtZero: true } }
            }
        });

        // Chart 2: Need Level Distribution (bar)
        new Chart(document.getElementById('needLevelChart'), {
            type: 'bar',
            data: {
                labels: ['متوسط', 'شدید', 'خیلی شدید'],
                datasets: [{
                    label: 'تعداد خانواده‌ها',
                    data: [40, 25, 15],
                    backgroundColor: colors[0],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false }, title: { display: true, text: 'توزیع خانواده‌ها بر اساس سطح نیاز' } },
                scales: { y: { beginAtZero: true } }
            }
        });

        // Chart 3: Families per Dist List (bar)
        new Chart(document.getElementById('distListChart'), {
            type: 'bar',
            data: {
                labels: ['لیست ۱', 'لیست ۲', 'لیست ۳', 'لیست ۴'],
                datasets: [{
                    label: 'تعداد خانواده‌ها',
                    data: [50, 30, 20, 10],
                    backgroundColor: colors[1],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false }, title: { display: true, text: 'تعداد خانواده‌ها در هر لیست توزیع' } },
                scales: { y: { beginAtZero: true } }
            }
        });

        // Chart 4: Orphans per Family (bar)
        new Chart(document.getElementById('orphansChart'), {
            type: 'bar',
            data: {
                labels: ['خانواده ۱', 'خانواده ۲', 'خانواده ۳', 'خانواده ۴'],
                datasets: [{
                    label: 'تعداد یتیمان',
                    data: [3, 5, 2, 4],
                    backgroundColor: colors[2],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false }, title: { display: true, text: 'تعداد افراد یتیم در هر خانواده' } },
                scales: { y: { beginAtZero: true } }
            }
        });

        // Chart 5: Package Distribution Over Time (bar)
        new Chart(document.getElementById('packageDistChart'), {
            type: 'bar',
            data: {
                labels: ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد'],
                datasets: [{
                    label: 'تعداد بسته‌ها',
                    data: [100, 120, 90, 150, 130],
                    borderColor: colors[3],
                    fill: false,
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false }, title: { display: true, text: 'توزیع بسته‌های حمایتی در طول زمان' } },
                scales: { y: { beginAtZero: true } }
            }
        });

        // Chart 6: Package Total Cost (bar)
        new Chart(document.getElementById('packageCostChart'), {
            type: 'bar',
            data: {
                labels: ['بسته ۱', 'بسته ۲', 'بسته ۳'],
                datasets: [{
                    label: 'هزینه کل (ریال)',
                    data: [50000000, 30000000, 20000000],
                    backgroundColor: colors.slice(0, 3),
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { position: 'top' }, title: { display: false, text: 'هزینه کل بسته‌های حمایتی' } }
            }
        });

        // Chart 7: Medical Aid Costs (bar)
        new Chart(document.getElementById('medicalAidChart'), {
            type: 'bar',
            data: {
                labels: ['خانواده ۱', 'خانواده ۲', 'خانواده ۳'],
                datasets: [{
                    label: 'هزینه (ریال)',
                    data: [10000000, 15000000, 8000000],
                    backgroundColor: colors[4],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false }, title: { display: true, text: 'هزینه کمک‌های پزشکی' } },
                scales: { y: { beginAtZero: true } }
            }
        });

        // Chart 8: Supporter Support Count (bar)
        new Chart(document.getElementById('supporterCountChart'), {
            type: 'bar',
            data: {
                labels: ['حامی ۱', 'حامی ۲', 'حامی ۳', 'حامی ۴'],
                datasets: [{
                    label: 'تعداد حمایت‌ها',
                    data: [10, 15, 8, 12],
                    backgroundColor: colors[5],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false }, title: { display: true, text: 'تعداد حمایت‌های حامیان' } },
                scales: { y: { beginAtZero: true } }
            }
        });

        // Chart 9: Support Amount Over Time (bar)
        new Chart(document.getElementById('supportAmountChart'), {
            type: 'bar',
            data: {
                labels: ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد'],
                datasets: [{
                    label: 'مبلغ (ریال)',
                    data: [5000000, 7000000, 6000000, 9000000, 8000000],
                    borderColor: colors[6],
                    fill: false,
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false }, title: { display: true, text: 'مبلغ حمایت‌های مالی در طول زمان' } },
                scales: { y: { beginAtZero: true } }
            }
        });

        // Chart 10: Observations Over Time (bar)
        new Chart(document.getElementById('observationsChart'), {
            type: 'bar',
            data: {
                labels: ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد'],
                datasets: [{
                    label: 'تعداد مشاهدات',
                    data: [20, 25, 15, 30, 22],
                    borderColor: colors[7],
                    fill: false,
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false }, title: { display: true, text: 'تعداد مشاهدات در طول زمان' } },
                scales: { y: { beginAtZero: true } }
            }
        });
