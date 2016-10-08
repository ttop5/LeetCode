/**
 * @param {number} numRows
 * @return {number[][]}
 */
function generate(numRows) {
  if (numRows === 0) {
    return [];
  }
  let numList = [[1]];
  for (let i=1; i<numRows; i++) {
    let preRow = numList[i-1];
    let newRow = [1];
    for (let j=1; j<i; j++) {
      newRow[j] = preRow[j-1] + preRow[j];
    }
    newRow.push(1);
    numList.push(newRow);
  }
  return numList;
}
