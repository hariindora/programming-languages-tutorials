main(List<String> args) {
  // var emp = new Emp();
  // emp.show_emp_info();
  var manager = new Manager();
  manager.show_emp_info();
  var engineer = new Engineer();
  engineer.show_emp_info();
  Emp E1 = new Manager();
  E1.show_emp_info();
}

abstract class Emp {
  void show_emp_info();
}

class Manager extends Emp {
  @override
  void show_emp_info() {
    print("Show info of Manager");
  }

  void show_salary() {
    print("800000");
  }
}

class Engineer extends Emp {
  @override
  void show_emp_info() {
    print("Show info of Engineer");
  }

  void show_salary() {
    print("800000");
  }
}
