// parser.js
class Node {
  constructor(type, value) {
    this.type = type;
    this.value = value;
  }
}

class Parser {
  constructor(input) {
    this.input = input;
    this.pos = 0;
  }

  eat(type) {
    if (this.input[this.pos].type === type) {
      this.pos++;
      return true;
    }
    return false;
  }

  parse() {
    const result = [];
    while (this.pos < this.input.length) {
      const node = this.parseExpression();
      if (node) {
        result.push(node);
      }
    }
    return result;
  }

  parseExpression() {
    if (this.eat('LPAREN')) {
      const result = this.parseLine();
      if (this.eat('RPAREN')) {
        return new Node('expression', result);
      } else {
        throw new Error('Expected RPAREN');
      }
    } else {
      return this.parseLine();
    }
  }

  parseLine() {
    const result = [];
    while (this.pos < this.input.length && this.input[this.pos].type !== 'EOL') {
      const node = this.parseTerm();
      if (node) {
        result.push(node);
      }
    }
    return result;
  }

  parseTerm() {
    const result = [];
    while (this.pos < this.input.length && this.input[this.pos].type !== 'OP') {
      const node = this.parseFactor();
      if (node) {
        result.push(node);
      }
    }
    return result;
  }

  parseFactor() {
    if (this.eat('NUMBER')) {
      return new Node('number', this.input[this.pos - 1].value);
    } else if (this.eat('LPAREN')) {
      const result = this.parseLine();
      if (this.eat('RPAREN')) {
        return result;
      } else {
        throw new Error('Expected RPAREN');
      }
    } else {
      throw new Error('Expected factor');
    }
  }
}

class Token {
  constructor(type, value) {
    this.type = type;
    this.value = value;
  }
}

const input = [
  new Token('LPAREN', '('),
  new Token('NUMBER', '5'),
  new Token('OP', '+'),
  new Token('NUMBER', '3'),
  new Token('RPAREN', ')'),
  new Token('EOL', '\n'),
];

const parser = new Parser(input);
const result = parser.parse();
console.log(result);