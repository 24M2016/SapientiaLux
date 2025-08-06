import 'package:flutter/material.dart';
import 'screens/grammar_screen.dart';

void main() {
  runApp(const SapientiaLuxApp());
}

class SapientiaLuxApp extends StatelessWidget {
  const SapientiaLuxApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SapientiaLux',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const GrammarScreen(),
    );
  }
}