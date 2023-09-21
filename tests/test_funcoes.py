import pytest

from app import add_usuario, ver_usuario

@pytest.mark.add_usuario_email
def test_add_usuario_email_sem_arroba():
    assert add_usuario('Luigi',19,'12345678901','rua aaaa','luigiquinzi.com') == False

@pytest.mark.add_usuario_email
def test_add_usuario_email_sem_carac_apos_arroba():
    assert add_usuario('Luigi',19,'12345678901','rua aaaa','luigiquinzi@') == False

@pytest.mark.add_usuario_idade
def test_add_usuario_idade_negativa():
    assert add_usuario('Luigi',-12,'12345678901','rua aaaa','luigiquinzi@gmail.com') == False

@pytest.mark.add_usuario_idade
def test_add_usuario_idade_maior_120():
    assert add_usuario('Luigi',130,'12345678901','rua aaaa','luigiquinzi@gmail.com') == False

@pytest.mark.add_usuario_cpf
def test_add_user_cpf_menor():
    assert add_usuario('Luigi',19,'1234567890','rua aaaa','luigiquinzi@gmail.com') == False

@pytest.mark.add_usuario_cpf
def test_add_user_cpf_maior():
    assert add_usuario('Luigi',19,'123456789011','rua aaaa','luigiquinzi@gmail.com') == False

@pytest.mark.add_usuario
def test_add_user_certo():
    assert add_usuario('Luigi',19,'12345678901','rua aaaa','luigiquinzi@gmail.com') == 'Usuário Cadastrado'

@pytest.mark.ver_user
def test_ver_user_certo():
    assert ver_usuario(3) == [(3,'Charlie',40,'34567890123','Praça dos Chocolate, 7','charlie@chocolate.com')]

@pytest.mark.ver_user
def test_ver_user_id_nao_existe():
    assert ver_usuario(15) == []







