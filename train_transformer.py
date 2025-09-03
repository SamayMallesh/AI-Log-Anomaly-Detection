import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset
import pandas as pd
from sklearn.preprocessing import LabelEncoder

class LogDataset(Dataset):
    def __init__(self, csv_file):
        df = pd.read_csv(csv_file)
        self.logs = df['message'].values
        self.labels = torch.tensor(LabelEncoder().fit_transform(df['level']))
    
    def __len__(self):
        return len(self.logs)
    
    def __getitem__(self, idx):
        return self.logs[idx], self.labels[idx]

class SimpleTransformer(nn.Module):
    def __init__(self, vocab_size=1000, embed_dim=32, num_classes=3):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.transformer_layer = nn.TransformerEncoderLayer(embed_dim, nhead=2)
        self.transformer = nn.TransformerEncoder(self.transformer_layer, num_layers=2)
        self.fc = nn.Linear(embed_dim, num_classes)
    
    def forward(self, x):
        x = self.embedding(x)
        x = self.transformer(x)
        x = x.mean(dim=1)
        return self.fc(x)

if __name__ == "__main__":
    dataset = LogDataset('../data/sample_logs.csv')
    loader = DataLoader(dataset, batch_size=2, shuffle=True)
    
    model = SimpleTransformer()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    for epoch in range(5):
        for logs, labels in loader:
            # Placeholder: convert logs to random token indices for demo
            inputs = torch.randint(0, 999, (labels.size(0), 10))
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch} Loss: {loss.item()}")
