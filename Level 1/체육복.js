function solution(n, lost, reserve) {
  const newLost = lost.filter((value) => !reserve.includes(value));
  const newReserve = reserve.filter((value) => !lost.includes(value));

  for (let i = 0; i < newLost.length; i++) {
    const ele = newLost[i];
    if (newReserve.includes(ele - 1)) {
      newLost.splice(i, 1);
      newReserve.splice(newReserve.indexOf(ele - 1), 1);
      i--;
    } else if (newReserve.includes(ele + 1)) {
      newLost.splice(i, 1);
      newReserve.splice(newReserve.indexOf(ele + 1), 1);
      i--;
    }
  }

  const answer = n - newLost.length;
  return answer;
}
