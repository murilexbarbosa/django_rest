from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from rest_framework.fields import SerializerMethodField
from atracoes.models import Atracao
from enderecos.models import Endereco


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer(many=False)
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes',
                  'comentarios', 'avaliacoes', 'endereco', 'descricao_completa',
                  'descricao_completa2')
        read_only_fields = ('comentarios', 'avaliacoes')

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        ##carregando atracoes
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        ##carregando endereco
        endereco = validated_data['endereco']
        del validated_data['endereco']

        ##criando objeto ponto turistico
        ponto = PontoTuristico.objects.create(**validated_data)

        ##preenchendo atracoes ao objeto ponto turistico
        self.cria_atracoes(atracoes, ponto)

        ##preenchendo endereco ao objeto ponto turistico
        end = Endereco.objects.create(**endereco)
        ponto.endereco = end

        ponto.save()
        ##retornando objeto para gravação
        return ponto


    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
