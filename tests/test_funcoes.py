import pytest

from app import add_usuario, ver_usuario, att_user, del_user

@pytest.mark.add_usuario
def test_add_usuario_email_sem_arroba():
    assert add_usuario('Luigi',19,'12345678901','rua aaaa','luigiquinzi.com') == False

@pytest.mark.add_usuario
def test_add_usuario_email_sem_carac_apos_arroba():
    assert add_usuario('Luigi',19,'12345678901','rua aaaa','luigiquinzi@') == False

@pytest.mark.add_usuario
def test_add_usuario_idade_negativa():
    assert add_usuario('Luigi',-12,'12345678901','rua aaaa','luigiquinzi@gmail.com') == False

@pytest.mark.add_usuario
def test_add_usuario_idade_maior_120():
    assert add_usuario('Luigi',130,'12345678901','rua aaaa','luigiquinzi@gmail.com') == False

@pytest.mark.add_usuario
def test_add_user_cpf_menor():
    assert add_usuario('Luigi',19,'1234567890','rua aaaa','luigiquinzi@gmail.com') == False

@pytest.mark.add_usuario
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

@pytest.mark.edit_user
def test_edita_user_nao_existe():
    assert att_user(20,{'nome' : 'Luis'}) == 'Usuário não encontrado'

@pytest.mark.edit_user
def test_edita_user_cpf_errado():
    assert att_user(8,{'cpf' : '1234567890'}) == 'Cpf precisa ter 11 digitos'

@pytest.mark.edit_user
def test_edita_user_email_errado():
    assert att_user(7,{'email' : 'socratesmorreu'}) == 'Email irregular'

@pytest.mark.edit_user
def test_edita_user_email_errado2():
    assert att_user(9,{'email' : 'socratesmorreu@'}) == 'Email irregular'

@pytest.mark.edit_user
def test_edita_user_idade_errada():
    assert att_user(6,{'idade' : 140}) == 'Idade irregular'

@pytest.mark.edit_user
def test_edita_user_um_input_certo():
    assert att_user(10,{'nome':'Luis'}) == 'Usuário atualizado com sucesso'

@pytest.mark.edit_user
def test_edita_user_varios_inputs_certos():
    assert att_user(7,{'email' : 'socratesmorreu@gmail.com','nome': 'henrique','idade':18,'cpf':'12445678901'})

@pytest.mark.deleta_user
def test_deleta_usuario_inexistente():
    assert del_user(19) == 'Usuário não encontrado'

@pytest.mark.deleta_user
def test_deleta_usuario_existente():
    assert del_user(9) == 'Usuário deletado'