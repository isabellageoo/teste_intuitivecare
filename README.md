A API da ANS não permite a listagem automática de diretórios ou arquivos, nem responde adequadamente a requisições HEAD ou scraping HTML.
Diante disso, optou-se por uma abordagem determinística baseada no calendário, assumindo os três últimos trimestres completos como entrada para o processamento.
Essa decisão prioriza simplicidade, previsibilidade e robustez.

A função de cálculo automático de trimestres foi mantida, porém para garantir reprodutibilidade do teste, utilizei trimestres com dados já publicados