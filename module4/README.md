## Описание работы модуля Г(4)
	
	1. Для Запуска Веб-сервера вам понадобится Bun(https://bun.sh/), установка: "curl -fsSL https://bun.sh/install | bash" (Также можно использовать node.js(npm/pnpm) для запуска)

	2. Запуск веб-сервера из chvt2026_Shilov_Nikita_9: cd module4/RMC_Panel/ && bun run dev

	3. Для запуска Бекенд сервера вам понадобится Python пакет "Flask" (https://flask.palletsprojects.com/en/stable/)
	
	4. нужно создать окружение для flask из chvt2026_Shilov_Nikita_9: python3 -m venv .venv

	5. когда появится в консоли (.venv), значит вы уже в окружение, теперь настройка: pip install flask

	6. дальше запуск самого бекенд сервера из chvt2026_Shilov_Nikita_9: python3 module4/RMC_Panel/src/backend/api.py

	7. Дальше можете заходить на веб панель на: http://localhost:5173/

	Функционал: 
		Реализованы кнопки движения вперед и Экстренная кнопка сброса скорости(движения), также вывод батареи