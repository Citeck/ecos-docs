Развертывание нового сервера
==============================

Генерация уникального ключа шифрования
---------------------------------------

1. При развертывании нового сервера необходимо каждый раз генерировать уникальный ключ шифрования.
2. Используйте следующий код для генерации AES-ключа:

.. code-block::

    fun main() {

        val keyGen = KeyGenerator.getInstance("AES")
        keyGen.init(128) // AES key size 128
        val secretKey = keyGen.generateKey()
        val base64Key = Base64.getEncoder().encodeToString(secretKey.encoded)

        println("Base64 Key: $base64Key")

    } 

3. Убедитесь, что ключ по умолчанию заменен на новый. Если этого не сделать, система выдаст предупреждение в логах.

:ref:`Подробнее о шифровании секретов<secrets_encryption>`