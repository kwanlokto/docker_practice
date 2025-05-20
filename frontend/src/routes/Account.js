import {
  Box,
  Button,
  List,
  ListItem,
  ListItemText,
  TextField,
  Typography
} from '@material-ui/core';
import { createTransaction, getAllTransactions } from '../data-handler/auth';
import { useEffect, useState } from 'react';

import { useParams } from 'react-router-dom';

export const AccountDetail = () => {
  const { accountId } = useParams();
  const [transactions, setTransactions] = useState([]);
  const [value, setValue] = useState('');
  const [operation, setOperation] = useState('');

  const fetchTransactions = async () => {
    const response = await getAllTransactions(accountId);
    console.log(response.data.data)
    setTransactions(response.data.data);
  };

  useEffect(() => {
    fetchTransactions();
  }, [accountId]);

  const handleCreateTransaction = async () => {
    if (!value || !operation) return;
    try {
      await createTransaction(accountId, operation, parseFloat(value));
      setValue('');
      setOperation('');
      fetchTransactions();
    } catch (err) {
      console.error('Failed to create transaction', err);
    }
  };

  return (
    <Box sx={{ p: 4, maxWidth: 800, mx: 'auto' }}>
      <Typography variant="h5" gutterBottom>
        Transactions for Account #{accountId}
      </Typography>

      {/* Transaction creation form */}
      <Box display="flex" flexDirection="column" mb={4}>
        <TextField
          label="Operation"
          value={operation}
          onChange={(e) => setOperation(e.target.value)}
          margin="normal"
        />
        <TextField
          label="Value"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          type="number"
          margin="normal"
        />
        <Button variant="contained" color="primary" onClick={handleCreateTransaction}>
          Add Transaction
        </Button>
      </Box>

      {/* Transaction list */}
      <List>
        {transactions.map((transaction) => (
          <ListItem key={transaction.id}>
            <ListItemText
              primary={`$${transaction.value} — ${transaction.operation}`}
              secondary={`Transaction ID: ${transaction.id}`}
            />
          </ListItem>
        ))}
      </List>
    </Box>
  );
};
