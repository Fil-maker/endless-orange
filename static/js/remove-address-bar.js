// Сначала получаем высоту окна просмотра 
// и умножаем ее на 1%
let vh = window.innerHeight * 0.01;

// Затем устанавливаем значение свойства --vh
// для корневого элемента
document.documentElement.style.setProperty('--vh', `${vh}px`);


// слушаем событие resize
window.addEventListener('resize', () => {
    // получаем текущее значение высоты
    let vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);
});