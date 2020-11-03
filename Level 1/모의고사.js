const answers = [1, 2, 3, 4, 5];

function solution(answers) {
  const Human = [
    { id: 1, pattern: [1, 2, 3, 4, 5], answer: 0 },
    { id: 2, pattern: [2, 1, 2, 3, 2, 4, 2, 5], answer: 0 },
    { id: 3, pattern: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5], answer: 0 },
  ];

  for (let i = 0; i < Human.length; i++) {
    Human[i].answer = answers.filter(
      (answer, index) =>
        answer === Human[i].pattern[index % Human[i].pattern.length]
    ).length;
  }

  Human.sort(function (a, b) {
    return a.answer < b.answer ? 1 : a.answer > b.answer ? -1 : 0;
  });

  const answer = Human.filter((human) => human.answer === Human[0].answer).map(
    (human) => human.id
  );
  return answer;
}

console.log(solution(answers));
