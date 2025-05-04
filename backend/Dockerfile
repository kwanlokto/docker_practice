FROM python:3.7

WORKDIR /app/backend

# Copy pre-made requirements.txt
COPY requirements.txt ./

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the app code
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
