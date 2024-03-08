
import datetime
import json

class Note:
	# Класс для представления отдельной Заметки:
	def __init__ (self, title, content, creation_date):
		self.title = title
		self.content = content
		self.creation_date = creation_date
		
class NoteManager:
	# Класс для работы с Заметками:
	def __init__ (self, file_path):
		self.file_path = file_path
		self.notes = []
		
	def load_notes(self):
		with open(self.file_path, 'r', encoding='utf-8') as file:
			self.json_notes = json.load(file)
			for note in self.json_notes:
				note_object = Note(note['title'], note['content'], note['creation_date'])
				self.notes.append(note_object)
	# Добавление заметки:			
	def add_note(self, note):
		self.notes.append(note)

    # Редактирование заметки:	
	def edit_note(self, note_index, new_title, new_content):
		self.notes[note_index].title = new_title
		self.notes[note_index].content = new_content

    # Удаление заметки:	
	def delete_note(self, note_index):
		del self.notes[note_index]
		
    # Чтение списка заметок:
	def print_notes(self):
		for i, note in enumerate(self.notes):
			print(f'Заметка {i}: {note.title}\n\t Содержание: {note.content}\n\t Дата создания: {note.creation_date}')

	def save_notes(self):
		with open(self.file_path, mode='w', encoding='utf-8') as f:
			json_notes = [{'title': note.title,'content': note.content, 'creation_date': note.creation_date} for note in self.notes]
			json.dump(json_notes, f)

if __name__ == '__main__':
	file_path = "notes.json"

	manager = NoteManager(file_path)
	manager.load_notes()

while True:
	print('\n\tМеню\n'
			'1. Чтение списка заметок\n'
			'2. Добавление заметки\n'
			'3. Редактирование заметки\n'
			'4. Удаление заметки\n'
			'0. Выйти из программы')
	cmd = input('\t> выберите пункт меню: ')

	if cmd == '1':
		# Чтение списка заметок:
		manager.print_notes()
	elif cmd == '2':
		# Добавление заметки:
		real_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
		notel = Note('ИЗМЕНИТЬ заголовок!', 'ДОБАВИТЬ содержание!', real_date)
		manager.add_note(notel)
		manager.save_notes()
		manager.print_notes()
	elif cmd == '3':
		# Редактирование заметки:
		note_index = int (input ('\tВведите номер заметки для редактирования: '))
		new_title = str (input ('\tВведите новый заголовок: '))
		new_content = str (input ('\tВведите новый контент: '))    
		manager.edit_note(note_index, new_title, new_content)
		manager.save_notes()
		manager.print_notes()
	elif cmd == '4':
		# Удаление заметки:
		note_index = int (input ('\tВведите номер заметки для удаления: '))
		manager.delete_note(note_index)
		manager.save_notes()
		manager.print_notes()
	elif cmd == "0":
		print('\tЗавершение работы программы')
		break

