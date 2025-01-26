contract MyContract {
    uint public value1;
    uint public value2;

    function add() public returns (uint) {
        return 1 + 2 * 4 - 2;
    }
    function mul() public returns (uint) {
        return 10 * 7;
    }
}