# Guia de Configuração do Interruptor _TZE204_unsxl4ir (TS0601) com ZHA no Home Assistant

## 1. 📦 Preparação do Ambiente

**Pré-requisitos:**
- Home Assistant com ZHA habilitado.
- Acesso root ao sistema de arquivos do host (ou Supervisor).
- File Editor habilitado ou acesso por SSH.

---

## 2. 🗂️ Criar o Diretório de Quirks Personalizados

```bash
mkdir -p /var/lib/homeassistant/homeassistant/custom_zha_quirks
```

Crie o arquivo `__init__.py` com o seguinte conteúdo:
```python
from .tuya_unsxl4ir import TuyaQuadSwitchTZE204
```

> 💡 Esse caminho equivale a `/config/custom_zha_quirks` no contexto do Home Assistant.

---

## 3. 🛠️ Criar a Quirk Personalizada

1. Crie o arquivo `tuya_unsxl4ir.py` no mesmo diretório.
2. Insira o conteúdo completo da quirk personalizada (_TZE204_unsxl4ir).
```python
Conteúdo de tuya
```

---

## 4. ⚙️ Editar o configuration.yaml

Edite o arquivo `/config/configuration.yaml` e adicione:

```yaml
zha:
  custom_quirks_path: /config/custom_zha_quirks
```

---

## 5. 🔁 Reiniciar o Home Assistant

Reinicie o Home Assistant via interface ou terminal:

```bash
ha core restart
```

---

## 6. 🔄 Reparear o Dispositivo

1. Vá em **Configurações > Dispositivos e Serviços > ZHA > Configurar**
2. Remova o dispositivo _TZE204_unsxl4ir
3. Adicione novamente em modo de pareamento
4. Verifique se agora aparecem **4 entidades de luz**

---

## 7. 🧠 Testar Automação

Crie uma automação usando sensor de presença como gatilho e `light.tuya_quad_switch_x` como ação.

---

## ✅ Resultado Esperado

- Dispositivo com 4 canais totalmente operacionais no ZHA
- Funcionamento com sensores, automações e UI do Home Assistant

---

## 📎 Referências

- [ZHA Device Handlers (zha-quirks)](https://github.com/zigpy/zha-device-handlers)
- Discussões sobre _TZE204_unsxl4ir no GitHub
