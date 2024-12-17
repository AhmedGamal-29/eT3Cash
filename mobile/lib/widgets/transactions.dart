import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

class TransactionList extends StatelessWidget {
  final List<Map<String, dynamic>> transactions;

  const TransactionList({required this.transactions});

  @override
  Widget build(BuildContext context) {
    // Reverse the transactions list to show the newest first
    final reversedTransactions =
        List<Map<String, dynamic>>.from(transactions.reversed);

    return ListView.builder(
      itemCount: reversedTransactions.length,
      shrinkWrap: true,
      physics: NeverScrollableScrollPhysics(),
      itemBuilder: (context, index) {
        return TransactionItem(transaction: reversedTransactions[index]);
      },
    );
  }
}

class TransactionItem extends StatelessWidget {
  final Map<String, dynamic> transaction;

  const TransactionItem({required this.transaction});

  @override
  Widget build(BuildContext context) {
    // Determine the icon, color, and label based on the transaction type
    IconData icon;
    Color color;
    String label = transaction['title'];

    switch (transaction['title']) {
      case 'cash_in':
        icon = Icons.arrow_downward;
        color = Colors.green;
        label = 'Cash In';
        break;
      case 'cash_out':
        icon = Icons.arrow_upward;
        color = Colors.red;
        label = 'Cash Out';
        break;
      case 'transfer':
        icon = Icons.compare_arrows;
        color = Colors.blue;
        label = 'Transfer';
        break;
      case 'donation':
        icon = Icons.volunteer_activism;
        color = Colors.orange;
        label = 'Donation';
        break;
      case 'investment':
        icon = Icons.trending_up;
        color = Colors.purple;
        label = 'Investment';
        break;
      default:
        icon = Icons.attach_money;
        color = Colors.grey;
        label = 'Transaction';
    }

    // Format the date using intl package
    DateTime transactionDate = DateTime.parse(transaction['date']);
    String formattedDate =
        DateFormat('MMMM dd, yyyy – hh:mm a').format(transactionDate);

    return Card(
      margin: const EdgeInsets.symmetric(vertical: 8.0),
      child: ListTile(
        leading: CircleAvatar(
          backgroundColor:
              color.withOpacity(0.1), // Lighter background for icon
          child: Icon(icon, color: color),
        ),
        title: Text(
          label,
          style: TextStyle(
            fontWeight: FontWeight.bold,
            color: color,
          ),
        ),
        subtitle: Text('$formattedDate'), // Use formatted date
        trailing: Text(
          '${transaction['amount'] > 0 ? '+' : ''}${transaction['amount'].toString()}',
          style: TextStyle(
            color: color,
            fontSize: 16.0,
            fontWeight: FontWeight.bold,
          ),
        ),
      ),
    );
  }
}
