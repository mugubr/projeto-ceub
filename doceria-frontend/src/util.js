import dayjs from "dayjs";
import 'dayjs/locale/pt-br.js'
const apiUrl = 'http://localhost:8000'

export function getPedidos()
{
  fetch(`${apiUrl}/pedidos`)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}

export function getMonth(month = dayjs().month()) {
  month = Math.floor(month);
  const year = dayjs().year();
  const firstDayOfTheMonth = dayjs(new Date(year, month, 1)).day();
  let currentMonthCount = 0 - firstDayOfTheMonth;
  const daysMatrix = new Array(5).fill([]).map(() => {
    return new Array(7).fill(null).map(() => {
      currentMonthCount++;
      return dayjs(new Date(year, month, currentMonthCount));
    });
  });
  return daysMatrix;
}

export function formatDate(date, format) {
    return dayjs(date).locale('pt-br').format(format);
  }