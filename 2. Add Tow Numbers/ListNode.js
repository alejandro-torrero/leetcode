class ListNode {
  constructor(value, next) {
    this.value = value;
    this.nextNode = next;
  }

  val() {
    return this.value;
  }

  next() {
    return this.nextNode;
  }

  print() {
    console.log("Value: ", this.value);
    if (this.nextNode != undefined) {
      this.nextNode.print();
    } else {
      console.log("Next node: undefined");
    }
  }
}

export default ListNode;
