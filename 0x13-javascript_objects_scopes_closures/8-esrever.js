#!/usr/bin/node

exports.esrever = function (list) {
  let listA = 0;
  let listB = list.length - 1;
  while (listA < listB) {
    const tmp = list[listA];
    list[listA] = list[listB];
    list[listB] = tmp;
    listA++;
    listB--;
  }
  return list;
};
