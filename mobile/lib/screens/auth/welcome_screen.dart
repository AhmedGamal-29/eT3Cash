import 'dart:async';
import 'package:flutter/material.dart';
import 'package:smart_wallet_app/screens/auth/login_screen.dart';

class WelcomeScreen extends StatefulWidget {
  static const id = "welcome_screen";
  const WelcomeScreen({Key? key}) : super(key: key);

  @override
  State<WelcomeScreen> createState() => _WelcomeScreenState();
}

class _WelcomeScreenState extends State<WelcomeScreen> {
  @override
  void initState() {
    super.initState();
    Timer(
        const Duration(seconds: 3),
        () => Navigator.pushReplacement(
            context, MaterialPageRoute(builder: (context) => LoginScreen())));
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.blue[50],
      child: const Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Image(
            image: AssetImage('assets/images/logo.png'),
          ),
          DefaultTextStyle(
            style: TextStyle(color: Colors.blueAccent, fontSize: 40.0),
            child: Text('eT3 Cash ..'),
          ),
        ],
      ),
    );
  }
}
