import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

class ApiService {
  static const String baseUrl = 'http://127.0.0.1:8000/api/';

  // Helper: Store token
  Future<void> storeToken(String token) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    await prefs.setString('auth_token', token);
  }

  // Helper: Retrieve token
  Future<String?> getToken() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    return prefs.getString('auth_token');
  }

  // Helper: Create headers with token
  Future<Map<String, String>> _getHeaders() async {
    final token = await getToken();
    if (token == null) throw Exception('Authorization token is missing');
    return {
      'Content-Type': 'application/json',
      'Authorization': 'Token $token',
    };
  }

  // Register API
  Future<Map<String, dynamic>> register(
      String username, String email, String phone, String password) async {
    final url = Uri.parse('${baseUrl}register/');
    final response = await http.post(
      url,
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'username': username,
        'email': email,
        'phone_number': phone,
        'password': password,
      }),
    );

    if (response.statusCode == 201) {
      return jsonDecode(response.body);
    } else {
      return {'error': 'Failed to register: ${response.body}'};
    }
  }

  // Login API
  Future<Map<String, dynamic>> login(String username, String password) async {
    final url = Uri.parse('${baseUrl}login/');
    final response = await http.post(
      url,
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'username': username,
        'password': password,
      }),
    );

    if (response.statusCode == 200) {
      final responseData = jsonDecode(response.body);
      await storeToken(responseData['token']);
      return responseData;
    } else {
      return {'error': 'Failed to login: ${response.body}'};
    }
  }

  // Fetch market data
  Future<Map<String, dynamic>?> getMarketData() async {
    try {
      final headers = await _getHeaders();
      final url = Uri.parse('${baseUrl}market-data/');
      final response = await http.get(url, headers: headers);

      if (response.statusCode == 200) {
        return jsonDecode(response.body) as Map<String, dynamic>;
      } else {
        return {'error': 'Failed to fetch market data: ${response.body}'};
      }
    } catch (e) {
      return {'error': 'Error: $e'};
    }
  }

  // Check balance API
  Future<double?> checkBalance() async {
    try {
      final headers = await _getHeaders();
      final url = Uri.parse('${baseUrl}check-balance/');
      final response = await http.get(url, headers: headers);

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        return double.tryParse(data['balance'].toString());
      } else {
        return null;
      }
    } catch (e) {
      return null;
    }
  }

  // Fetch transactions
  Future<List<Map<String, dynamic>>?> fetchTransactions() async {
    try {
      final headers = await _getHeaders();
      final url = Uri.parse('${baseUrl}transactions/');
      final response = await http.get(url, headers: headers);

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body) as List;
        return data.map((transaction) {
          return {
            'title': transaction['transaction_type'],
            'amount': double.tryParse(transaction['amount'].toString()) ?? 0.0,
            'recipient': transaction['recipient'] ?? 'N/A',
            'date': transaction['date'],
          };
        }).toList();
      } else {
        return null;
      }
    } catch (e) {
      return null;
    }
  }

  // Cash-in transaction
  Future<Map<String, dynamic>> cashIn(double amount) async {
    return _postTransaction('cash-in/', {
      'amount': amount,
      'transaction_type': 'cash_in',
    });
  }

  // Cash-out transaction
  Future<Map<String, dynamic>> cashOut(double amount) async {
    return _postTransaction('cash-out/', {
      'amount': amount,
      'transaction_type': 'cash_out',
    });
  }

  // Donation transaction
  Future<Map<String, dynamic>> donate(double amount) async {
    return _postTransaction('donate/', {
      'amount': amount,
      'transaction_type': 'donation',
    });
  }

  // Investment transaction
  Future<Map<String, dynamic>> invest(double amount,
      {required String stockSymbol}) async {
    return _postTransaction('invest/', {
      'amount': amount,
      'transaction_type': 'investment',
      'symbol': stockSymbol,
    });
  }

  // Transfer funds
  Future<Map<String, dynamic>> transfer(double amount, String recipient) async {
    return _postTransaction('transfer/', {
      'amount': amount,
      'recipient': recipient,
      'transaction_type': 'transfer',
    });
  }

  // Helper: Execute POST transaction
  Future<Map<String, dynamic>> _postTransaction(
      String endpoint, Map<String, dynamic> data) async {
    try {
      final headers = await _getHeaders();
      final url = Uri.parse('$baseUrl$endpoint');
      final response =
          await http.post(url, headers: headers, body: jsonEncode(data));

      if (response.statusCode == 200 || response.statusCode == 201) {
        return jsonDecode(response.body);
      } else {
        return {'error': 'Transaction failed: ${response.body}'};
      }
    } catch (e) {
      return {'error': 'Error: $e'};
    }
  }
}
