const array = [1, 5, 2, 6, 3, 7, 4],
  commands = [
    [2, 5, 3],
    [4, 4, 1],
    [1, 7, 3],
  ];

function solution(array, commands) {
  const answer = commands.map(
    (a) => array.slice(a[0] - 1, a[1]).sort((b, c) => b - c)[a[2] - 1]
  );

  // const answer = [];

  // for (let i = 0; i < commands.length; i++) {
  //   let result = array
  //     .slice(commands[i][0] - 1, commands[i][1])
  //     .sort((a, b) => a - b)[commands[i][2] - 1];
  //   answer.push(result);
  // }

  return answer;
}

console.log(solution(array, commands));
