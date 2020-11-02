const numbers = [5, 0, 2, 7];

function solution(numbers) {
  const result = [];
  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      if (i !== j) {
        const sum = numbers[i] + numbers[j];
        result.push(sum);
      }
    }
  }
  result.sort((a, b) => a - b);
  const answer = result.filter((value, index) => value !== result[index + 1]);
  // const answer = [...new Set(result)];
  return answer;
}

console.log(solution(numbers));
