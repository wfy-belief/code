import typing

from py2neo import Graph, Node, Relationship, NodeMatcher


# https://cloud.tencent.com/developer/article/1434904


class MyNeo4j(object):
    """docstring for My_neo4j"""
    __slots__ = '__graph'

    def __init__(self,
                 scheme: str = 'bolt',
                 host: str = 'localhost',
                 user: str = 'neo4j',
                 password: str = 'wfy'):
        """
        Args:
            scheme: 协议类型 默认 bolt(速度快-稳定) 可选 http
            host: 主机IP 默认 localhost
            user: 用户名 默认 neo4j
            password: 密码 默认 wfy
        """
        try:
            # 连接neo4j数据库，输入协议，地址、用户名、密码
            self.__graph = Graph(scheme=scheme,
                                 host=host,
                                 user=user,
                                 password=password
                                 )
        except Exception as e:
            print(e)
        else:
            print('连接成功', self.__graph)
        finally:
            print(self.__graph.call.dbms.components())

    def delete_all(self) -> None:
        """
        Returns:
            None 清除neo4j中原有的结点等所有信息
        """
        self.__graph.delete_all()
        print('清除neo4j中原有的结点等所有信息成功')
        return None

    def add_relationship(self,
                         source: typing.Dict,
                         relationship: str,
                         target: typing.Dict,
                         source_type: typing.List[str] = ('paper',),
                         target_type: typing.List[str] = ('person',)) -> None:
        """
        description:
            构造两个节点 和 关系的名字 生成关系
        Args:
            source: 类型 dict 传递一个字典,必须包含 'name' 其它键不限制
            relationship: 类型 str 传递一个字符串 表示关系
            target:类型 dict 传递一个字典,必须包含 'name' 其它键不限制
            source_type (List):List 元素字符串 列表元组都可以 表示source标签 可以是多标签
            target_type (List):List 元素字符串 列表元组都可以 表示target标签 可以是多标签

        Returns:
            None
        """
        # 转换为Node类型
        source = self.dict_to_node(source_type, source)
        target = self.dict_to_node(target_type, target)
        # 创建关系
        relation = Relationship(source, relationship, target)
        self.__graph.create(relation)
        return None

    def dict_to_node(self, label: typing.List[str], dict_data: typing.Dict) -> Node:
        """
        description:
            把数据转换为Node节点类型
        Args:
            label: Tuple[str]节点的标签
            dict_data: Dict[str] = str 节点的树形 name 键必须含有

        Returns:
            1.如果节点存在返回原节点
            2.如果节点不存在新建一个节点
            3.标签可以少查询多 不能多标签查询少标签数据
        """
        matcher = NodeMatcher(self.__graph)
        # 如果结点存在直接返回
        node = matcher.match(*label, **dict_data).first()
        if node:
            return node
        return Node(*label, **dict_data)
