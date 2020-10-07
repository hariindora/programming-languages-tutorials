void main(List<String> args) {
  var test = Test();
  var temp = test.show_name();
  print(temp);
}

class Person {
  String name = "";

  String show_name() {
    return name;
  }

  String walk() {
    return "person walk";
  }

  String talk() {
    return "person talk";
  }
}

class Bill {
  String Profession = "";

  String show_profession() {
    return Profession;
  }
}

class Test implements Person, Bill {
  @override
  String name = "jack";

  @override
  String show_name() {
    return name;
  }

  @override
  String walk() {
    return "person walk";
  }

  @override
  String talk() {
    return "person talk";
  }

  @override
  String Profession = "coder";

  @override
  String show_profession() {
    return Profession;
  }
}

// Rules for Implementing Interfaces:
// 1. A class that implements the interface must override every method and instance variable of an interface.
// 2. Dart doesn't provide syntax to declare the interface directly. The class declaration can consider as the interface itself.
// 3. An interface class must provide the full implementation of all the methods belong to the interfaces.
// 4. We can implement one or more interfaces simultaneously.
// 5. Using the interface, we can achieve multiple inheritance.
