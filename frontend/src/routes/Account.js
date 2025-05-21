import {
  Box,
  Button,
  IconButton,
  List,
  ListItem,
  ListItemText,
  TextField,
  Typography,
} from '@material-ui/core';
import { createTransaction, getAllTransactions } from '../data-handler/auth';
import { useEffect, useState } from 'react';
import { useHistory, useParams } from 'react-router-dom';

import CloseIcon from '@material-ui/icons/Close';

export const AccountDetail = () => {
  const { accountId } = useParams();
  const history = useHistory();

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
      console.error('Transaction failed', err);
    }
  };

  const isAddDisabled = !operation || !value || Number(value) <= 0;

  return (
    <Box sx={{ p: 3, maxWidth: 600, mx: 'auto' }}>
      {/* Header */}
      <Box
        display="flex"
        justifyContent="space-between"
        alignItems="center"
        mb={3}
        px={2}
      >
        <Typography variant="h6">Account #{accountId} Transactions</Typography>
        <IconButton onClick={() => history.push('/')}>
          <CloseIcon />
        </IconButton>
      </Box>

      {/* Transaction Form */}
      <Box sx={{ p: 2, mb: 4 }}>
        <Box
          display="flex"
          sx={{ gap: '16px' }}
          alignItems="center"
          flexWrap="wrap"
        >
          <TextField
            label="Operation"
            value={operation}
            onChange={(e) => setOperation(e.target.value)}
            size="small"
            sx={{ flexGrow: 1 }}
          />
          <TextField
            label="Value"
            type="number"
            value={value}
            onChange={(e) => setValue(e.target.value)}
            inputProps={{ min: 0, step: '0.01' }}
            size="small"
            sx={{ width: 120 }}
          />
          <Button
            variant="contained"
            onClick={handleCreateTransaction}
            disabled={isAddDisabled}
          >
            Add
          </Button>
        </Box>
      </Box>

      {/* Transaction List */}
      <Box>
        <List>
          {transactions.map(({ id, value, operation, created_at }) => (
            <ListItem key={id} divider>
              <ListItemText
                primary={`${
                  operation.charAt(0).toUpperCase() + operation.slice(1)
                } — $${Number(value).toFixed(2)}`}
                secondary={new Date(created_at).toLocaleString()}
              />
            </ListItem>
          ))}
        </List>
      </Box>
    </Box>
  );
};
