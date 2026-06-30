import ListNode from "./ListNode.js";

// Create lists

// const l1Array = [2,4,3]; // Actual value 342
// const l2Array = [5,6,4]; // Actual value 465
// result a ListNode [7,0,8]

const l1Array = [9,9,9];
const l2Array = [9,9];

const createList = (listArray) => {
  let resultList = null;
  let nextNode = undefined;

  for (let i = listArray.length - 1; i >= 0; i--) {
    const val = listArray[i];

    if (i == 0) {
      // Last element
      resultList = new ListNode(val, nextNode);
    } else {
      nextNode = new ListNode(val, nextNode);
    }
  }

  return resultList;
};

let l1 = createList(l1Array);
let l2 = createList(l2Array);

let listResult = null;

function addNumbers(node1, node2, carry = 0, isFirst = false) {
  const n1 = node1?.val() || 0;
  const n2 = node2?.val() || 0;

  let r = n1 + n2 + carry;

  let currentValue = r % 10;
  let carryOn = r >= 10 ? 1 : 0;

  let nextNode = undefined;

  const nextNode1 = node1?.next() || undefined
  const nextNode2 = node2?.next() || undefined

  if (nextNode1 || nextNode2 || carryOn)
    nextNode = addNumbers(nextNode1, nextNode2, carryOn);

  // create node
  if (isFirst) {
    // First operation defines the final listResult
    listResult = new ListNode(currentValue, nextNode);
  } else {
    return new ListNode(currentValue, nextNode);
  }
}

addNumbers(l1, l2, 0, true);

let tempNode = listResult;
let arrayResult = [];
while (tempNode != undefined) { 
  arrayResult.push(tempNode.val());
  tempNode = tempNode.next();
}

console.log(arrayResult)
console.log(arrayResult.toReversed().join(""));
