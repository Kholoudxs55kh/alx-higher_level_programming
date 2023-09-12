#!/usr/bin/node

exports.esrever = function (list) {
  const arrList = Array.from(list);
  let startIdx = 0;
  let endIdx = arrList.length - 1;
  while (startIdx < endIdx) {
    // swapping
    const temp = arrList[startIdx];
    arrList[startIdx] = arrList[endIdx];
    arrList[endIdx] = temp;
    startIdx++;
    endIdx--;
  }
  return (arrList);
};
