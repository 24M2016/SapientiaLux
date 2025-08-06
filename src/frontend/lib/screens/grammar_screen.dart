import 'package:flutter/material.dart';

class GrammarScreen extends StatefulWidget {
  const GrammarScreen({super.key});

  @override
  _GrammarScreenState createState() => _GrammarScreenState();
}

class _GrammarScreenState extends State<GrammarScreen> {
  final TextEditingController _controller = TextEditingController();
  String _result = '';
  String _explanation = '';

  // Placeholder for Python backend call
  void _correctGrammar(String text) {
    // done : Integrate with Python backend via FFI or local server
    Future<void> _correctGrammar(String text) async {
    try {
      final response = await http.post(
        Uri.parse('http://localhost:5000/correct'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'text': text}),
      );
      final result = jsonDecode(response.body);
      setState(() {
        _result = result['corrected_text'];
        _explanation = result['explanation'];
      });
    } catch (e) {
      setState(() {
        _result = 'Error';
        _explanation = 'Failed to connect to backend: $e';
      });
    }
  }
    setState(() {
      _result = text; // Placeholder
      _explanation = 'Checking grammar... (Placeholder)';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('SapientiaLux - Grammar Correction'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            TextField(
              controller: _controller,
              decoration: const InputDecoration(
                labelText: 'Enter text to correct',
                border: OutlineInputBorder(),
              ),
              maxLines: 3,
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: () {
                if (_controller.text.isNotEmpty) {
                  _correctGrammar(_controller.text);
                }
              },
              child: const Text('Correct Grammar'),
            ),
            const SizedBox(height: 16),
            if (_result.isNotEmpty) ...[
              const Text(
                'Corrected Text:',
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
              Text(_result, style: const TextStyle(fontSize: 16)),
              const SizedBox(height: 8),
              const Text(
                'Explanation:',
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
              Text(_explanation, style: const TextStyle(fontSize: 16)),
            ],
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
}