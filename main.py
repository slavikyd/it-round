from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QHBoxLayout, QDialog, QLineEdit, QLabel, QComboBox
import sys


class Editor(QWidget):
	def __init__(self):
		super(Editor, self).__init__()
		self.setWindowTitle('Fast notes')
		self.resize(600, 500)
	
		self.textEditor = QTextEdit()
		
		self.btnNew = QPushButton('Создать...')
		self.btnNew.clicked.connect(lambda:self.newOnClick())

		self.btnSave = QPushButton('Сохранить...')
		self.btnSave.clicked.connect(lambda:self.saveDlg())
		
		self.btnMenu = QPushButton('Назад в меню...') 
		self.btnMenu.clicked.connect(lambda:self.openDlg())
		
		self.btnCopy = QPushButton('📄')
		self.btnPaste = QPushButton('📋')
		self.btnCut = QPushButton('✂️')

		self.btnUndo = QPushButton('⬅')
		self.btnRedo = QPushButton('➡')

		UndoRedoLayout = QHBoxLayout()
		UndoRedoLayout.addWidget(self.btnUndo)
		UndoRedoLayout.addWidget(self.btnRedo)

		TextOperationsLayout = QVBoxLayout()
		TextOperationsLayout.addWidget(self.btnCopy)
		TextOperationsLayout.addWidget(self.btnPaste)
		TextOperationsLayout.addWidget(self.btnCut)

		FileOperationsLayout = QVBoxLayout()
		FileOperationsLayout.addWidget(self.btnNew)
		FileOperationsLayout.addWidget(self.btnSave)
		FileOperationsLayout.addWidget(self.btnMenu)

		ButtonsLayout = QHBoxLayout()
		ButtonsLayout.addLayout(TextOperationsLayout)
		ButtonsLayout.addLayout(FileOperationsLayout)

		MainLayout = QVBoxLayout()
		MainLayout.addLayout(UndoRedoLayout)
		MainLayout.addWidget(self.textEditor)
		MainLayout.addLayout(ButtonsLayout)
		

		self.setLayout(MainLayout)
	
	def newOnClick(self):
		self.textEditor.clear()

	def saveOnClick(self, format:int, name:str):
		formats = ['txt', 'md', 'html']
		try:
			with open(f'{name}.{formats[format]}', 'w') as f:
				if formats[format] == 'html':
					f.write(self.textEditor.toHtml())
				else:
					f.write(self.textEditor.toPlainText())
		except Exception:
			with open(f'{name}.{formats[format]}', 'x') as f:
				if formats[format] == 'html':
					f.write(self.textEditor.toHtml())
				else:
					f.write(self.textEditor.toPlainText())
	
	def openOnClick(self, format:int, name:str):
		formats = ['txt', 'md', 'html']
		file = f'{name}.{formats[format]}'
		try:
			with open(f'{name}.{formats[format]}') as f:
				self.textEditor.setPlainText(f.read())
		except Exception:
			dlg = QDialog()
			label = QLabel('Файла не существует')
			layout = QVBoxLayout()
			layout.addWidget(label)
			dlg.setLayout(layout)
			dlg.exec_()

	def openDlg(self):
		dlg = QDialog(self)
		dlg.setWindowTitle('Открыть файл...')
	
		infoLabel1 = QLabel('Введите название файла: ')
		infoLabel2 = QLabel('Выберите формат файла: ')
		
		inputName = QLineEdit()
		self.setFormat = QComboBox()
		btnExit = QPushButton('Отменить')
		btnApply = QPushButton('Открыть')
		dlgLayout = QVBoxLayout()
		inputLayout = QHBoxLayout()
		formatLayout = QHBoxLayout()
		buttonsLayout = QHBoxLayout()

		self.setFormat.addItems(['Обычный текст (.txt)', 'Markdown-файл (.md)', 'HTML-документ (.html)'])

		btnExit.clicked.connect(lambda:dlg.reject())
		btnApply.clicked.connect(lambda:self.openOnClick(self.setFormat.currentIndex(), inputName.text()))

		buttonsLayout.addWidget(btnExit)
		buttonsLayout.addWidget(btnApply)

		inputLayout.addWidget(infoLabel1)
		inputLayout.addWidget(inputName)

		formatLayout.addWidget(infoLabel2)
		formatLayout.addWidget(self.setFormat)

		dlgLayout.addLayout(inputLayout)
		dlgLayout.addLayout(formatLayout)
		dlgLayout.addLayout(buttonsLayout)
	
		dlg.setLayout(dlgLayout)
		dlg.exec_()

	def saveDlg(self):
		dlg = QDialog(self)
		dlg.setWindowTitle('Сохранение...')
	
		infoLabel1 = QLabel('Введите название файла: ')
		infoLabel2 = QLabel('Выберите формат файла: ')
		
		inputName = QLineEdit()
		self.setFormat = QComboBox()
		btnExit = QPushButton('Отменить')
		btnApply = QPushButton('Сохранить')
		dlgLayout = QVBoxLayout()
		inputLayout = QHBoxLayout()
		formatLayout = QHBoxLayout()
		buttonsLayout = QHBoxLayout()

		self.setFormat.addItems(['Обычный текст (.txt)', 'Markdown-файл (.md)', 'HTML-документ (.html)'])

		btnExit.clicked.connect(lambda:dlg.reject())
		btnApply.clicked.connect(lambda:self.saveOnClick(self.setFormat.currentIndex(), inputName.text()))

		buttonsLayout.addWidget(btnExit)
		buttonsLayout.addWidget(btnApply)

		inputLayout.addWidget(infoLabel1)
		inputLayout.addWidget(inputName)

		formatLayout.addWidget(infoLabel2)
		formatLayout.addWidget(self.setFormat)

		dlgLayout.addLayout(inputLayout)
		dlgLayout.addLayout(formatLayout)
		dlgLayout.addLayout(buttonsLayout)
	
		dlg.setLayout(dlgLayout)
		dlg.exec_()

app = QApplication(sys.argv)
win = Editor()
win.show()
sys.exit(app.exec_())
