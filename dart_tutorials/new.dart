import "dart:io";

main(List<String> args) {
  print("enter your fav. colour name");
  String colour = stdin.readLineSync();
  print("your fav. colour is: ${colour}");
  print("end of main");
}
