const n = 125;

function solution(n) {
  const three = n.toString(3);
  const threeReversed = [...three].reverse().join("");
  const ten = parseInt(threeReversed, 3);

  return ten;
}

console.log(solution(n));
