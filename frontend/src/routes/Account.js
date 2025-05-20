import {
  Box,
  Button,
  List,
  ListItem,
  ListItemText,
  MenuItem,
  Select,
  TextField,
  Typography,
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
    try {
      const response = await getAllTransactions(accountId);
      setTransactions(response.data.data);
    } catch (error) {
      console.error('Failed to fetch transactions', error);
    }
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

  const isAddDisabled = !operation || !value || Number(value) <= 0;

  return (
    <Box sx={{ p: 4, maxWidth: 600, mx: 'auto' }}>
      <Typography variant="h5" gutterBottom>
        Transactions for Account #{accountId}
      </Typography>

      <Box
        mb={4}
        sx={{ gap: 8, alignItems: 'center', flexWrap: 'wrap', display: 'flex' }}
      >
        <TextField
          label="Operation"
          value={operation}
          onChange={(e) => setOperation(e.target.value)}
          type="string"
        />

        <TextField
          label="Value"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          type="number"
          inputProps={{ min: 0, step: '0.01' }}
          sx={{ flexGrow: 1, minWidth: 100 }}
        />

        <Button
          variant="contained"
          color="primary"
          onClick={handleCreateTransaction}
          disabled={isAddDisabled}
          sx={{ height: 40 }}
        >
          Add
        </Button>
      </Box>

      <List>
        {transactions.map(({ id, value, operation, created_at }) => (
          <ListItem key={id} divider>
            <ListItemText
              primary={`${
                operation.charAt(0).toUpperCase() + operation.slice(1)
              }: $${Number(value).toFixed(2)}`}
              secondary={`Transaction ID: ${id} — ${new Date(
                created_at,
              ).toLocaleString()}`}
            />
          </ListItem>
        ))}
      </List>
    </Box>
  );
};
