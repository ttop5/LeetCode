/**
 * @param {number} rowIndex
 * @return {number[]}
 */
const getRow = function(rowIndex) {
  let numList = [];
  for(let i=0; i<(rowIndex + 1); i++) {
    numList.push([1]);  // 在列表中生成一个新的列表并将第一个置为1
    for(let j=1; j<(i + 1); j++) {
      if(i == j) {
        numList[i].push(1);  // 将每个子列表中的最后一个设置为1
      }else{
        numList[i].push(numList[i - 1][j] + numList[i - 1][j - 1]);
      }
    }
  }
  return numList[rowIndex]
};
