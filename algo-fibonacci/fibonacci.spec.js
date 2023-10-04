const fibonacci = require("./fibonacci");

describe("test fibonacci", () => {
  test("fibonacci(0) === 0", () => {
    expect(fibonacci(0)).toBe(0);
  });

  test("fibonacci(2) === 1", () => {
    expect(fibonacci(2)).toBe(1);
  });

  test("fibonacci(5) === 3", () => {
    expect(fibonacci(5)).toBe(3);
  });

  test("fibonacci(8) === 13", () => {
    expect(fibonacci(8)).toBe(13);
  });

  test("fibonacci(11) === 55", () => {
    expect(fibonacci(11)).toBe(55);
  });
});
