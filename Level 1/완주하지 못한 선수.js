const participant = ["m", "j", "n", "v", "f"];
const completion = ["j", "f", "m", "n"];

function solution(participant, completion) {
  const P = participant.sort();
  const C = completion.sort();
  const answer = P.filter((v, i) => v !== C[i])[0];
  return answer;
}

console.log(solution(participant, completion));
