# 🟢 F1L3 S3RV3R 🟢

A simple **local file server** for easy file transfers between environments.  
Useful for situations where traditional file sharing doesn't work well, especially in **VMs (Virtual Machines)**, sandbox environments, or isolated networks.

**Developer:** jc0818

---

## 📁 Features

✅ Upload and download files via a web browser  
✅ Automatic file storage in the `/shared` directory  
✅ Real-time file list display  
✅ Accessible from other devices in the same network  

---

## 🎯 Why I Made This

Transferring files between different environments can sometimes be annoying, especially when:

- You are working inside **Virtual Machines (VMs)** and drag & drop or shared folders don't work properly  
- The environment is isolated, and other transfer tools are restricted  
- You want a quick, minimal solution without setting up complex services  

This project provides a lightweight, browser-based file transfer tool, ideal for those quick use cases.

---
## 📂 Project Structure

```bash
project/
├── app.py           # Main server script
├── shared/             # Folder for uploaded and shared files
└── README.md
```

---

## 🚀 How to Run

**Requirements:**  
- Python 3.x  
- Flask library  

**Installation and Launch**

```bash
# Install Flask
pip install flask

# Run the server
python app.py
