import { Box, List, ListItem, ListItemText, Typography } from '@material-ui/core';
import { useEffect, useState } from 'react';

import { getAllTransactions } from '../data-handler/auth';
import { useParams } from 'react-router-dom';

export const AccountDetail = () => {
  const { accountId } = useParams();
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await getAllTransactions(accountId);
      setTransactions(response.data.data);
    };
    fetchData();
  }, [accountId]);

  return (
    <Box sx={{ p: 4, maxWidth: 800, mx: 'auto' }}>
      <Typography variant="h5" gutterBottom>
        Transactions for Account #{accountId}
      </Typography>
      <List>
        {transactions.map((transaction) => (
          <ListItem key={transaction.id}>
            <ListItemText
              primary={`$${transaction.value.toFixed(2)}`}
              secondary={new Date(transaction.created_at).toLocaleString()}
            />
          </ListItem>
        ))}
      </List>
    </Box>
  );
};
