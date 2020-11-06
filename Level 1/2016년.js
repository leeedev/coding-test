const a = 5,
  b = 24;

function solution(a, b) {
  const day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  const name = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"];
  const daySum = day.slice(0, a - 1).reduce((a, b) => a + b, 0) + b;

  const answer = name[daySum % 7];
  return answer;
}

console.log(solution(a, b));
